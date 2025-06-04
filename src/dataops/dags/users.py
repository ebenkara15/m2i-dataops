from datetime import datetime
from typing import Any

import pendulum
import requests
from airflow.decorators import dag, task
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    first_name: str
    last_name: str
    city: str
    country: str
    email: str = Field(pattern=r"^\S+@\S+\.\S+$")
    created_at: datetime
    age: int


@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def users_pipeline() -> None:
    """
    ### TaskFlow API Tutorial Documentation
    This is a simple data pipeline example which demonstrates the use of
    the TaskFlow API using three simple tasks for Extract, Transform, and Load.
    Documentation that goes along with the Airflow TaskFlow API tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """

    @task(show_return_value_in_logs=True)
    def extract() -> list | None:
        """
        ## Extract
        A simple Extract task to get data ready for the rest of the data
        pipeline. In this case, getting data is done by requesting an API
        with randomized users.
        """
        API_URL = "https://randomuser.me/api/"

        response = requests.get(url=API_URL, params={"results": "1000"})

        if not response.ok:
            response.raise_for_status()

        data: dict[str, Any] = response.json()

        return data.get("results")

    @task(show_return_value_in_logs=True)
    def validate(raw_users: list) -> list[User]:
        """
        ## Validation task
        A simple Validation task which takes in the collection of order data and
        computes the total order value.
        """
        valid_users: list[User] = []

        for u in raw_users:
            try:
                user = User(
                    first_name=u["name"]["first"],
                    last_name=u["name"]["last"],
                    city=u["location"]["city"],
                    country=u["location"]["country"],
                    email=u["email"],
                    created_at=u["registered"]["date"],
                    age=u["dob"]["age"],
                )

                valid_users.append(user.model_dump_json())
            except KeyError as e:
                print(f"🔴 There is a missing key for the user: {u}")
                print(e)
            except ValidationError as e:
                print(f"🔴 There is a problem validating the user: {u}")
                print(e)

        return valid_users

    @task()
    def load(valid_users: list):
        """
        #### Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """

        print(f"🔴 Total number of valid users: {len(valid_users)}")

    raw_users = extract()
    valid_users = validate(raw_users)
    load(valid_users) >> dummy_task


users_pipeline()

if __name__ == "__main__":
    users_pipeline().test()

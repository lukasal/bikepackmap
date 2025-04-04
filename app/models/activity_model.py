from pydantic import BaseModel, ValidationError, Field, Extra
from typing import List, Optional, Any, Tuple
from datetime import date
import pandas as pd
import uuid

class Activity(BaseModel):
    name: str
    id: str =  Field(default_factory=lambda: str(uuid.uuid4()), description="The unique identifier for the activity")
    start_date: Optional[pd.Timestamp]
    end_date: Optional[pd.Timestamp]
    date: Optional[date] 
    type: str
    map_polyline: List[Tuple[float, float]]
    start_latlng: List[float]
    end_latlng: List[float]
    map_elevation: Optional[List[float]] = Field(None)
    map_distance: Optional[List[float]] = Field(None)
    start_location: Optional[str] = Field(None)
    end_location: Optional[str] = Field(None)
    metadata: dict
    source: str
    ready: bool

    class Config:
        arbitrary_types_allowed = True
        extra = 'ignore'  # Ignore extra fields

    @staticmethod
    def get_field_names() -> List[str]:
        """
        Returns a list of field names (or aliases) for the Activity model.
        """
        return [field.alias if field.alias else field.name for field in Activity.__fields__.values()]

    @staticmethod
    def convert_df(activities: pd.DataFrame) -> List["Activity"]:
        """
        Validates a pandas DataFrame containing activity data and converts it to a DataFrame of validated activity data.

        Args:
            activities (pd.DataFrame): The DataFrame to validate.

        Returns:
            pd.DataFrame: A DataFrame of validated activity data.

        Raises:
            ValidationError: If any row in the DataFrame fails validation.
        """
        activities_dict = activities.to_dict(orient="records")
        validated_activities = []
        error_count = 0
        for activity in activities_dict:
            try:
                validated_activity = Activity(**activity)
                validated_activities.append(validated_activity)
            except ValidationError as e:
                error_count += 1
                print(f"Validation error for activity: {activity['name']}, error: {e}")
        if error_count > 0:
            print(f"{error_count} activies where discarded because they do not contain valid tracks.")
            # print warning to user
        return validated_activities

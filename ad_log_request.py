from typing import Optional

from pydantic import BaseModel


class AdlogsGHExtractionRequest(BaseModel):
    start: str
    end: str
    campaign_line_name: str
    raw_adlogs_ghs_path: str
    refined_destination_path: str
    final_destination_path: str
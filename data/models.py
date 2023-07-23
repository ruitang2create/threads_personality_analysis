from pydantic import BaseModel
from typing import Optional, List, Dict

class ProfilePic(BaseModel):
    height: int
    url: str
    width: int

class InstagramUser(BaseModel):
    is_private: bool 
    profile_pic_url: str
    username: str
    hd_profile_pic_versions: List[ProfilePic]
    is_verified: bool
    biography: Optional[str] = None
    biography_with_entities: Optional[str] = None
    follower_count: int
    pk: str

class InstagramProfilePicUrls(BaseModel):
    height: int
    url: str
    width: int


class PostUser(BaseModel):
    profile_pic_url: str
    username: str 
    id: Optional[int] = None
    is_verified: bool
    pk: str

class Post(BaseModel):
    user: PostUser
    image_versions2: dict 
    original_width: int
    original_height: int
    caption: dict
    like_count: int
    id: str

class ReplyUser(BaseModel):
    profile_pic_url: str
    id: Optional[int] = None

class ThreadItem(BaseModel):
    post: Post
    reply_facepile_users: List[ReplyUser]

class Thread(BaseModel):
    thread_items: List[ThreadItem]
    id: str
    
class UserThreadsResponse(BaseModel):
    data: Dict[str, Dict[str, Dict[str, Dict[str, Post]]]]
    extensions: dict
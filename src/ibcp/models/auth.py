from pydantic import BaseModel, Field


class ServerInfo(BaseModel):
    server_name: str | None = Field(None, alias="serverName")
    server_version: str | None = Field(None, alias="serverVersion")

    model_config = {"extra": "allow", "populate_by_name": True}


class AuthStatus(BaseModel):
    authenticated: bool
    competing: bool
    connected: bool
    message: str
    mac: str = Field("", alias="MAC")
    server_info: ServerInfo | None = Field(None, alias="serverInfo")
    hardware_info: str | None = Field(None, alias="hardware_info")
    fail: str = ""

    model_config = {"extra": "allow", "populate_by_name": True}


class HmdsInfo(BaseModel):
    error: str | None = None

    model_config = {"extra": "allow", "populate_by_name": True}


class IserverInfo(BaseModel):
    auth_status: AuthStatus = Field(..., alias="authStatus")

    model_config = {"extra": "allow", "populate_by_name": True}


class TickleResponse(BaseModel):
    session: str
    sso_expires: int = Field(..., alias="ssoExpires")
    collision: bool = Field(..., alias="collission")
    user_id: int = Field(..., alias="userId")
    hmds: HmdsInfo | None = None
    iserver: IserverInfo | None = None

    model_config = {"extra": "allow", "populate_by_name": True}


class AuthStatusResponse(AuthStatus):
    pass


class ReauthenticateResponse(BaseModel):
    message: str

    model_config = {"extra": "allow", "populate_by_name": True}


class LogoutResponse(BaseModel):
    status: bool

    model_config = {"extra": "allow", "populate_by_name": True}

import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._identity_verification_requested_customer import IdentityVerificationRequestedCustomer
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class ReadyIdentityVerification:
    """준비 상태의 본인인증 내역"""
    status: Literal["READY"] = dataclasses.field()
    """본인인증 상태"""
    id: str = dataclasses.field()
    """본인인증 내역 아이디"""
    channel: Optional[SelectedChannel] = dataclasses.field()
    """사용된 본인인증 채널"""
    requested_customer: IdentityVerificationRequestedCustomer = dataclasses.field(metadata={"serde_rename": "requestedCustomer"})
    """요청 시 고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData"})
    """사용자 지정 데이터"""
    requested_at: str = dataclasses.field(metadata={"serde_rename": "requestedAt"})
    """본인인증 요청 시점"""
    updated_at: str = dataclasses.field(metadata={"serde_rename": "updatedAt"})
    """업데이트 시점"""
    status_changed_at: str = dataclasses.field(metadata={"serde_rename": "statusChangedAt"})
    """상태 업데이트 시점"""


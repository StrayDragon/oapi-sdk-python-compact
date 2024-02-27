# Code generated by lark suite oapi sdk gen

from typing import List
from ....utils.dt import to_json_decorator
import attr


@to_json_decorator
@attr.s
class WorkLocation:
    id = attr.ib(type=int, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class WorkExperience:
    company = attr.ib(type=str, default=None, metadata={"json": "company"})
    department = attr.ib(type=str, default=None, metadata={"json": "department"})
    job = attr.ib(type=str, default=None, metadata={"json": "job"})
    start = attr.ib(type=str, default=None, metadata={"json": "start"})
    end = attr.ib(type=str, default=None, metadata={"json": "end"})
    description = attr.ib(type=str, default=None, metadata={"json": "description"})


@to_json_decorator
@attr.s
class NativeRegion:
    iso_code = attr.ib(type=str, default=None, metadata={"json": "iso_code"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class Manager:
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    en_name = attr.ib(type=str, default=None, metadata={"json": "en_name"})


@to_json_decorator
@attr.s
class JobLevel:
    id = attr.ib(type=int, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class Job:
    id = attr.ib(type=int, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class EmergencyContact:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    relationship = attr.ib(type=int, default=None, metadata={"json": "relationship"})
    mobile = attr.ib(type=str, default=None, metadata={"json": "mobile"})


@to_json_decorator
@attr.s
class Education:
    level = attr.ib(type=int, default=None, metadata={"json": "level"})
    school = attr.ib(type=str, default=None, metadata={"json": "school"})
    major = attr.ib(type=str, default=None, metadata={"json": "major"})
    degree = attr.ib(type=int, default=None, metadata={"json": "degree"})
    start = attr.ib(type=str, default=None, metadata={"json": "start"})
    end = attr.ib(type=str, default=None, metadata={"json": "end"})


@to_json_decorator
@attr.s
class CustomFields:
    key = attr.ib(type=str, default=None, metadata={"json": "key"})
    label = attr.ib(type=str, default=None, metadata={"json": "label"})
    type = attr.ib(type=str, default=None, metadata={"json": "type"})
    value = attr.ib(type=str, default=None, metadata={"json": "value"})


@to_json_decorator
@attr.s
class ContractCompany:
    id = attr.ib(type=int, default=None, metadata={"json": "id"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})


@to_json_decorator
@attr.s
class Attachment:
    id = attr.ib(type=str, default=None, metadata={"json": "id"})
    mime_type = attr.ib(type=str, default=None, metadata={"json": "mime_type"})
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    size = attr.ib(type=int, default=None, metadata={"json": "size"})


@to_json_decorator
@attr.s
class SystemFields:
    name = attr.ib(type=str, default=None, metadata={"json": "name"})
    en_name = attr.ib(type=str, default=None, metadata={"json": "en_name"})
    email = attr.ib(type=str, default=None, metadata={"json": "email"})
    mobile = attr.ib(type=str, default=None, metadata={"json": "mobile"})
    department_id = attr.ib(type=str, default=None, metadata={"json": "department_id"})
    manager = attr.ib(type=Manager, default=None, metadata={"json": "manager"})
    job = attr.ib(type=Job, default=None, metadata={"json": "job"})
    job_level = attr.ib(type=JobLevel, default=None, metadata={"json": "job_level"})
    work_location = attr.ib(type=WorkLocation, default=None, metadata={"json": "work_location"})
    gender = attr.ib(type=int, default=None, metadata={"json": "gender"})
    birthday = attr.ib(type=str, default=None, metadata={"json": "birthday"})
    native_region = attr.ib(type=NativeRegion, default=None, metadata={"json": "native_region"})
    ethnicity = attr.ib(type=int, default=None, metadata={"json": "ethnicity"})
    marital_status = attr.ib(type=int, default=None, metadata={"json": "marital_status"})
    political_status = attr.ib(type=int, default=None, metadata={"json": "political_status"})
    entered_workforce_date = attr.ib(type=str, default=None, metadata={"json": "entered_workforce_date"})
    id_type = attr.ib(type=int, default=None, metadata={"json": "id_type"})
    id_number = attr.ib(type=str, default=None, metadata={"json": "id_number"})
    hukou_type = attr.ib(type=int, default=None, metadata={"json": "hukou_type"})
    hukou_location = attr.ib(type=str, default=None, metadata={"json": "hukou_location"})
    bank_account_number = attr.ib(type=str, default=None, metadata={"json": "bank_account_number"})
    bank_name = attr.ib(type=str, default=None, metadata={"json": "bank_name"})
    social_security_account = attr.ib(type=str, default=None, metadata={"json": "social_security_account"})
    provident_fund_account = attr.ib(type=str, default=None, metadata={"json": "provident_fund_account"})
    employee_no = attr.ib(type=str, default=None, metadata={"json": "employee_no"})
    employee_type = attr.ib(type=int, default=None, metadata={"json": "employee_type"})
    status = attr.ib(type=int, default=None, metadata={"json": "status"})
    hire_date = attr.ib(type=str, default=None, metadata={"json": "hire_date"})
    probation_months = attr.ib(type=float, default=None, metadata={"json": "probation_months"})
    conversion_date = attr.ib(type=str, default=None, metadata={"json": "conversion_date"})
    application = attr.ib(type=int, default=None, metadata={"json": "application"})
    application_status = attr.ib(type=int, default=None, metadata={"json": "application_status"})
    last_day = attr.ib(type=str, default=None, metadata={"json": "last_day"})
    departure_type = attr.ib(type=int, default=None, metadata={"json": "departure_type"})
    departure_reason = attr.ib(type=int, default=None, metadata={"json": "departure_reason"})
    departure_notes = attr.ib(type=str, default=None, metadata={"json": "departure_notes"})
    contract_company = attr.ib(type=ContractCompany, default=None, metadata={"json": "contract_company"})
    contract_type = attr.ib(type=int, default=None, metadata={"json": "contract_type"})
    contract_start_date = attr.ib(type=str, default=None, metadata={"json": "contract_start_date"})
    contract_expiration_date = attr.ib(type=str, default=None, metadata={"json": "contract_expiration_date"})
    contract_sign_times = attr.ib(type=int, default=None, metadata={"json": "contract_sign_times"})
    personal_email = attr.ib(type=str, default=None, metadata={"json": "personal_email"})
    family_address = attr.ib(type=str, default=None, metadata={"json": "family_address"})
    primary_emergency_contact = attr.ib(
        type=EmergencyContact,
        default=None,
        metadata={"json": "primary_emergency_contact"},
    )
    emergency_contact = attr.ib(
        type=List[EmergencyContact],
        default=None,
        metadata={"json": "emergency_contact"},
    )
    highest_level_of_edu = attr.ib(type=Education, default=None, metadata={"json": "highest_level_of_edu"})
    education = attr.ib(type=List[Education], default=None, metadata={"json": "education"})
    former_work_exp = attr.ib(type=WorkExperience, default=None, metadata={"json": "former_work_exp"})
    work_exp = attr.ib(type=List[WorkExperience], default=None, metadata={"json": "work_exp"})
    id_photo_po_side = attr.ib(type=List[Attachment], default=None, metadata={"json": "id_photo_po_side"})
    id_photo_em_side = attr.ib(type=List[Attachment], default=None, metadata={"json": "id_photo_em_side"})
    id_photo = attr.ib(type=List[Attachment], default=None, metadata={"json": "id_photo"})
    diploma_photo = attr.ib(type=List[Attachment], default=None, metadata={"json": "diploma_photo"})
    graduation_cert = attr.ib(type=List[Attachment], default=None, metadata={"json": "graduation_cert"})
    cert_of_merit = attr.ib(type=List[Attachment], default=None, metadata={"json": "cert_of_merit"})
    offboarding_file = attr.ib(type=List[Attachment], default=None, metadata={"json": "offboarding_file"})
    cancel_onboarding_reason = attr.ib(type=int, default=None, metadata={"json": "cancel_onboarding_reason"})
    cancel_onboarding_notes = attr.ib(type=str, default=None, metadata={"json": "cancel_onboarding_notes"})
    employee_form_status = attr.ib(type=int, default=None, metadata={"json": "employee_form_status"})
    create_time = attr.ib(type=int, default=None, metadata={"json": "create_time"})
    update_time = attr.ib(type=int, default=None, metadata={"json": "update_time"})


@to_json_decorator
@attr.s
class Employee:
    user_id = attr.ib(type=str, default=None, metadata={"json": "user_id"})
    system_fields = attr.ib(type=SystemFields, default=None, metadata={"json": "system_fields"})
    custom_fields = attr.ib(type=List[CustomFields], default=None, metadata={"json": "custom_fields"})


@attr.s
class EmployeeListResult:
    items = attr.ib(type=List[Employee], default=None, metadata={"json": "items"})
    page_token = attr.ib(type=str, default=None, metadata={"json": "page_token"})
    has_more = attr.ib(type=bool, default=None, metadata={"json": "has_more"})

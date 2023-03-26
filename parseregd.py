import io
import json
from typing import TextIO

# str_json = '''
# {   "name": "staff",
#     "staff":[
#
#     {
#       "id": 4994590,
#       "created_at": "2017-06-15",
#       "updated_at": "2022-08-22",
#       "deleted_at": null,
#       "user_id": 4828781,
#       "gusoev_login": "agabekjands",
#       "name": "Агабекян Диана Сергеевна",
#       "school_id": 160,
#       "school_integration_id": 789,
#       "type": "teacher",
#       "roles": [
#         "teacher",
#         "ae_educator",
#         "staff"
#       ],
#       "mobility": "no",
#       "education_level_ids": [],
#       "deleted": false,
#       "workload": 18,
#       "subjects": [
#         {
#           "id": 33623611,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "Музыка",
#           "exam_name": null,
#           "subject_group_id": null,
#           "school_id": null,
#           "subject_status": null,
#           "is_curriculum_subject": false,
#           "is_discipline": false,
#           "only_group": false,
#           "is_adapt": false,
#           "is_spo": false,
#           "knowledge_field_ids": [],
#           "fgos_version_id": [],
#           "curriculum_subject_ids": null,
#           "curriculum_subjects": null,
#           "discipline_ids": null,
#           "disciplines": null,
#           "children_subjects": null,
#           "curriculum_subject_attributes": null,
#           "curriculum_levels": null,
#           "control_forms": null,
#           "knowledge_field_link": [],
#           "adapt_parameters": null,
#           "organization_id": null,
#           "integration_id": null,
#           "parent_subject_ids": null,
#           "education_level_ids": [
#             1,
#             2
#           ]
#         }
#       ],
#       "class_unit_ids": [],
#       "class_units": [],
#       "group_ids": [],
#       "managed_class_unit_ids": [],
#       "managed_class_units": [],
#       "building_ids": [
#         1262
#       ],
#       "building_integration_ids": [
#         907
#       ],
#       "buildings": [
#         {
#           "id": 1262,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "улица Крылатские Холмы 28 корп. 3 ",
#           "address": "Западный административный округ, муниципальный округ Крылатское, город Москва, улица Крылатские Холмы, дом 28, корпус 3",
#           "school_id": null,
#           "rooms_number": null,
#           "floor_count": null,
#           "number": null,
#           "postal_index": null,
#           "county": null,
#           "gusoev_county_key": null,
#           "district": null,
#           "gusoev_district_key": null,
#           "eo_address": null,
#           "gusoev_eu_key": null,
#           "eu": null,
#           "city": null,
#           "gusoev_kladr_key": null,
#           "street": null,
#           "gusoev_address_key": null,
#           "building": null,
#           "description": null,
#           "education_level_ids": null,
#           "capacity": null,
#           "unom": null,
#           "is_org_territory": null,
#           "image": null,
#           "type": null,
#           "school_integration_id": null,
#           "integration_id": 907
#         }
#       ],
#       "room_ids": [
#         78777
#       ],
#       "assigned_group_ids": [],
#       "assigned_ae_group_ids": [
#         22738762
#       ],
#       "assigned_ec_group_ids": [],
#       "rooms": [
#         {
#           "id": 78777,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "Музыкальный зал",
#           "number": "20",
#           "capacity": 30,
#           "responsible_id": null,
#           "room_type_id": null,
#           "floor": null,
#           "description": null,
#           "education_level_ids": [],
#           "subject_ids": [],
#           "teacher_ids": [],
#           "is_ae_education": null,
#           "is_subsidiary": null,
#           "is_administrative": null,
#           "building_id": 1262,
#           "building_integration_id": 907
#         }
#       ],
#       "comment": null,
#       "user": {
#         "last_name": "Агабекян",
#         "middle_name": "Сергеевна",
#         "first_name": "Диана",
#         "phone_number": "8 (903) 961-55-41",
#         "email": "diana91@yandex.ru",
#         "date_of_birth": "1965-03-17",
#         "login": "agabekjands",
#         "phone_number_ezd": "79039615541"
#       },
#       "user_integration_id": 33227194,
#       "virtual": false,
#       "is_gap_allowed": false,
#       "for_consideration": false,
#       "subject_ids": [
#         33623611
#       ],
#       "week_day_ids": [],
#       "teacher_week_days": [],
#       "replacement_groups_ids": [],
#       "is_newcomer": null
#     },
#     {
#       "id": 4416052,
#       "created_at": "2017-02-15",
#       "updated_at": "2022-08-22",
#       "deleted_at": null,
#       "user_id": 3813483,
#       "gusoev_login": "20052508a",
#       "name": "Азадова Зифа Хайдяровна",
#       "school_id": 160,
#       "school_integration_id": 789,
#       "type": "teacher",
#       "roles": [
#         "teacher",
#         "junior_educator",
#         "staff"
#       ],
#       "mobility": "no",
#       "education_level_ids": [],
#       "deleted": false,
#       "workload": 18,
#       "subjects": [
#         {
#           "id": 33623629,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "Изобразительное искусство",
#           "exam_name": null,
#           "subject_group_id": null,
#           "school_id": null,
#           "subject_status": null,
#           "is_curriculum_subject": false,
#           "is_discipline": false,
#           "only_group": false,
#           "is_adapt": false,
#           "is_spo": false,
#           "knowledge_field_ids": [],
#           "fgos_version_id": [],
#           "curriculum_subject_ids": null,
#           "curriculum_subjects": null,
#           "discipline_ids": null,
#           "disciplines": null,
#           "children_subjects": null,
#           "curriculum_subject_attributes": null,
#           "curriculum_levels": null,
#           "control_forms": null,
#           "knowledge_field_link": [],
#           "adapt_parameters": null,
#           "organization_id": null,
#           "integration_id": null,
#           "parent_subject_ids": null,
#           "education_level_ids": [
#             1,
#             2
#           ]
#         }
#       ],
#       "class_unit_ids": [],
#       "class_units": [],
#       "group_ids": [],
#       "managed_class_unit_ids": [
#         457486
#       ],
#       "managed_class_units": [
#         {
#           "id": 457486,
#           "display_name": "3",
#           "class_level_id": 14,
#           "home_based": false
#         }
#       ],
#       "building_ids": [
#         1263
#       ],
#       "building_integration_ids": [
#         906
#       ],
#       "buildings": [
#         {
#           "id": 1263,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "улица Крылатские Холмы 28 корп. 2 ",
#           "address": "Западный административный округ, муниципальный округ Крылатское, город Москва, улица Крылатские Холмы, дом 28, корпус 2",
#           "school_id": null,
#           "rooms_number": null,
#           "floor_count": null,
#           "number": null,
#           "postal_index": null,
#           "county": null,
#           "gusoev_county_key": null,
#           "district": null,
#           "gusoev_district_key": null,
#           "eo_address": null,
#           "gusoev_eu_key": null,
#           "eu": null,
#           "city": null,
#           "gusoev_kladr_key": null,
#           "street": null,
#           "gusoev_address_key": null,
#           "building": null,
#           "description": null,
#           "education_level_ids": null,
#           "capacity": null,
#           "unom": null,
#           "is_org_territory": null,
#           "image": null,
#           "type": null,
#           "school_integration_id": null,
#           "integration_id": 906
#         }
#       ],
#       "room_ids": [],
#       "assigned_group_ids": [],
#       "assigned_ae_group_ids": [
#         22743576
#       ],
#       "assigned_ec_group_ids": [],
#       "rooms": [],
#       "comment": null,
#       "user": {
#         "last_name": "Азадова",
#         "middle_name": "Хайдяровна",
#         "first_name": "Зифа",
#         "phone_number": "8 (917) 552-81-44",
#         "email": "aato2005@mail.ru",
#         "date_of_birth": "1976-09-18",
#         "login": "20052508a",
#         "phone_number_ezd": "79175528144",
#         "email_ezd": "aato2005@mail.ru"
#       },
#       "user_integration_id": 33207573,
#       "virtual": false,
#       "is_gap_allowed": false,
#       "for_consideration": false,
#       "subject_ids": [
#         33623629
#       ],
#       "week_day_ids": [],
#       "teacher_week_days": [],
#       "replacement_groups_ids": [],
#       "is_newcomer": null
#     },
#     {
#       "id": 4994600,
#       "created_at": "2017-06-15",
#       "updated_at": "2022-08-22",
#       "deleted_at": null,
#       "user_id": 4828792,
#       "gusoev_login": "aisinaef",
#       "name": "Айсина Эльмира Фаритовна",
#       "school_id": 160,
#       "school_integration_id": 789,
#       "type": "teacher",
#       "roles": [
#         "teacher",
#         "junior_educator",
#         "staff"
#       ],
#       "mobility": "no",
#       "education_level_ids": [],
#       "deleted": false,
#       "workload": 36,
#       "subjects": [],
#       "class_unit_ids": [],
#       "class_units": [],
#       "group_ids": [],
#       "managed_class_unit_ids": [
#         457493
#       ],
#       "managed_class_units": [
#         {
#           "id": 457493,
#           "display_name": "26",
#           "class_level_id": 14,
#           "home_based": false
#         }
#       ],
#       "building_ids": [
#         1261
#       ],
#       "building_integration_ids": [
#         908
#       ],
#       "buildings": [
#         {
#           "id": 1261,
#           "created_at": null,
#           "updated_at": null,
#           "deleted_at": null,
#           "name": "улица Крылатские Холмы 30 корп. 6 ",
#           "address": "Западный административный округ, муниципальный округ Крылатское, город Москва, улица Крылатские Холмы, дом 30, корпус 6",
#           "school_id": null,
#           "rooms_number": null,
#           "floor_count": null,
#           "number": null,
#           "postal_index": null,
#           "county": null,
#           "gusoev_county_key": null,
#           "district": null,
#           "gusoev_district_key": null,
#           "eo_address": null,
#           "gusoev_eu_key": null,
#           "eu": null,
#           "city": null,
#           "gusoev_kladr_key": null,
#           "street": null,
#           "gusoev_address_key": null,
#           "building": null,
#           "description": null,
#           "education_level_ids": null,
#           "capacity": null,
#           "unom": null,
#           "is_org_territory": null,
#           "image": null,
#           "type": null,
#           "school_integration_id": null,
#           "integration_id": 908
#         }
#       ],
#       "room_ids": [],
#       "assigned_group_ids": [],
#       "assigned_ae_group_ids": [
#         22743414,
#         22743424
#       ],
#       "assigned_ec_group_ids": [],
#       "rooms": [],
#       "comment": null,
#       "user": {
#         "last_name": "Айсина",
#         "middle_name": "Фаритовна",
#         "first_name": "Эльмира",
#         "phone_number": "+7 (916) 6650348",
#         "email": "tuter1641@mail.ru",
#         "date_of_birth": "1983-07-20",
#         "login": "aisinaef",
#         "phone_number_ezd": "79166650348",
#         "email_ezd": "tuter1641@mail.ru"
#       },
#       "user_integration_id": 33156320,
#       "virtual": false,
#       "is_gap_allowed": false,
#       "for_consideration": false,
#       "subject_ids": [],
#       "week_day_ids": [],
#       "teacher_week_days": [],
#       "replacement_groups_ids": [],
#       "is_newcomer": null
#     }
#     ]}'''
with io.open("staff_python.csv", "w") as staff_python:
    with io.open("staff.json", encoding="utf-8") as file_json:
        staff = json.load(file_json)

        for item in staff["staff"]:
            item_staff_type = item.get("type")
            item_staff_roles = item.get("roles")
            item_staff_subjects = item.get("subjects")
            item_staff_buildings = item.get("buildings")
            item_staff_rooms = item.get("rooms")
            item_staff_user = item.get("user") if item.get("user") is not None \
                else {'last_name': '', 'middle_name': '', 'first_name': '',
                      'phone_number': '', 'email': '', 'date_of_birth': '', 'login': ''}

            item_staff_rooms_name = [item_staff_rooms_name.get("name") for item_staff_rooms_name in item_staff_rooms] \
                if len([item_staff_rooms_name.get("name") for item_staff_rooms_name in item_staff_rooms]) \
                else ["None"]

            item_staff_rooms_number = [item_staff_rooms_number.get("number") for item_staff_rooms_number in
                                       item_staff_rooms] \
                if len([item_staff_rooms_name.get("name") for item_staff_rooms_name in item_staff_rooms]) \
                else ["None"]

            item_staff_subjects_name = [item_staff_subjects_name.get("name") for item_staff_subjects_name in
                                        item_staff_subjects] \
                if len([item_staff_subjects_name.get("name") for item_staff_subjects_name in item_staff_subjects]) \
                else ["None"]

            item_staff_buildings_name = [item_staff_buildings_name.get("name") for item_staff_buildings_name in
                                         item_staff_buildings] \
                if len([item_staff_buildings_name.get("name") for item_staff_buildings_name in item_staff_buildings]) \
                else ["None"]

            item_staff_user_last_name = item_staff_user.get("last_name")
            item_staff_user_middle_name = item_staff_user.get("middle_name")
            item_staff_user_first_name = item_staff_user.get("first_name")
            item_staff_user_phone_number = item_staff_user.get("phone_number")
            item_staff_user_date_of_birth = item_staff_user.get("date_of_birth")
            item_staff_user_login = item_staff_user.get("login")
            item_staff_user_email =  item_staff_user.get("email")

            # print(item_staff_type, item_staff_roles , *item_staff_subjects_name,
            #       [item_staff_buildings_name.get("name") for item_staff_buildings_name in item_staff_buildings],
            #       *item_staff_rooms_name, *item_staff_rooms_number,
            #       (item_staff_user.get("last_name"), item_staff_user.get("middle_name"), item_staff_user.get("first_name"),
            #         item_staff_user.get("phone_number"), item_staff_user.get("email"), item_staff_user.get("date_of_birth"),
            #         item_staff_user.get("login")) if item_staff_user is not None else " ", sep=";", file=staff_python
            #      )

            print(item_staff_user_last_name, item_staff_user_first_name,item_staff_user_middle_name,
                  item_staff_user_phone_number, item_staff_user_login, item_staff_user_email,item_staff_user_date_of_birth, item_staff_type,
                  ", ".join(item_staff_roles), ", ".join(item_staff_subjects_name),
                  ", ".join(item_staff_buildings_name),
                  ", ".join(item_staff_rooms_number), ",".join(item_staff_rooms_name), sep=";", file=staff_python)

staff_python.close()

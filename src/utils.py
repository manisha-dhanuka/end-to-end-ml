import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exceptions import CustomException
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report ={}

        for name in models.keys():
            model = models[name]
            para = params[name]
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = recall_score(y_train, y_train_pred)
            test_model_score = recall_score(y_test, y_test_pred)

            report[name] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e,sys)

def get_binary_encoded_columns():
    columns = ['Access_DRM_content._(S)',
            'Access_Email_provider_data_(S)',
            'Access_all_system_downloads_(S)',
            'Access_download_manager._(S)',
            'Advanced_download_manager_functions._(S)',
            'Audio_File_Access_(S)',
            'Install_DRM_content._(S)',
            'Modify_Google_service_configuration_(S)',
            'Modify_Google_settings_(S)',
            'Move_application_resources_(S)',
            'Read_Google_settings_(S)',
            'Send_download_notifications._(S)',
            'Voice_Search_Shortcuts_(S)',
            'access_SurfaceFlinger_(S)',
            'access_checkin_properties_(S)',
            'access_the_cache_filesystem_(S)',
            'access_to_passwords_for_Google_accounts_(S)',
            'act_as_an_account_authenticator_(S)',
            'bind_to_a_wallpaper_(S)',
            'bind_to_an_input_method_(S)',
            'change_screen_orientation_(S)',
            'coarse_(network-based)_location_(S)',
            'control_location_update_notifications_(S)',
            'control_system_backup_and_restore_(S)',
            'delete_applications_(S)',
            "delete_other_applications'_caches_(S)",
            "delete_other_applications'_data_(S)",
            'directly_call_any_phone_numbers_(S)',
            'directly_install_applications_(S)',
            'disable_or_modify_status_bar_(S)',
            'discover_known_accounts_(S)',
            'display_unauthorized_windows_(S)',
            'enable_or_disable_application_components_(S)',
            'force_application_to_close_(S)',
            'force_device_reboot_(S)',
            'full_Internet_access_(S)',
            'interact_with_a_device_admin_(S)',
            'manage_application_tokens_(S)',
            'mock_location_sources_for_testing_(S)',
            'modify_battery_statistics_(S)',
            'modify_secure_system_settings_(S)',
            'modify_the_Google_services_map_(S)',
            'modify/delete_USB_storage_contents_modify/delete_SD_card_contents_(S)',
            'monitor_and_control_all_application_launching_(S)',
            'partial_shutdown_(S)',
            'permanently_disable_device_(S)',
            'permission_to_install_a_location_provider_(S)',
            'power_device_on_or_off_(S)',
            'press_keys_and_control_buttons_(S)',
            'prevent_app_switches_(S)',
            'read_frame_buffer_(S)',
            'read_instant_messages_(S)',
            'read_phone_state_and_identity_(S)',
            'record_what_you_type_and_actions_you_take_(S)',
            'reset_system_to_factory_defaults_(S)',
            'run_in_factory_test_mode_(S)',
            'set_time_(S)',
            'set_wallpaper_size_hints_(S)',
            'start_IM_service_(S)',
            'update_component_usage_statistics_(S)',
            'write_contact_data_(S)',
            'write_instant_messages_(S)',
            'enable_application_debugging_(D)',
            'limit_number_of_running_processes_(D)',
            'make_all_background_applications_close_(D)',
            'send_Linux_signals_to_applications_(D)',
            'change_your_audio_settings_(D)',
            'control_flashlight_(S)',
            'control_vibrator_(S)',
            'record_audio_(D)',
            'take_pictures_and_videos_(D)',
            'test_hardware_(S)',
            'Broadcast_data_messages_to_applications._(S)',
            'control_Near_Field_Communication_(D)',
            'create_Bluetooth_connections_(D)',
            'download_files_without_notification_(S)',
            'full_Internet_access_(D)',
            'make/receive_Internet_calls_(D)',
            'receive_data_from_Internet_(S)',
            'view_Wi-Fi_state_(S)',
            'view_network_state_(S)',
            'intercept_outgoing_calls_(D)',
            'modify_phone_state_(S)',
            'read_phone_state_and_identity_(D)',
            'directly_call_phone_numbers_(D)',
            'send_SMS_messages_(D)',
            'Storage_:_modify/delete_USB_storage_contents_modify/delete_SD_card_contents_(D)',
            'allow_Wi-Fi_Multicast_reception_(D)',
            'automatically_start_at_boot_(S)',
            'bluetooth_administration_(D)',
            'change_Wi-Fi_state_(D)',
            'change_background_data_usage_setting_(S)',
            'change_network_connectivity_(D)',
            'change_your_UI_settings_(D)',
            'delete_all_application_cache_data_(D)',
            'disable_keylock_(D)',
            'display_system-level_alerts_(D)',
            'expand/collapse_status_bar_(S)',
            'force_stop_other_applications_(S)',
            'format_external_storage_(D)',
            'kill_background_processes_(S)',
            'make_application_always_run_(D)',
            'measure_application_storage_space_(S)',
            'modify_global_animation_speed_(D)',
            'modify_global_system_settings_(D)',
            'mount_and_unmount_filesystems_(D)',
            'prevent_device_from_sleeping_(D)',
            'read_subscribed_feeds_(S)',
            'read_sync_settings_(S)',
            'read_sync_statistics_(S)',
            'read/write_to_resources_owned_by_diag_(S)',
            'reorder_running_applications_(D)',
            'retrieve_running_applications_(D)',
            'send_package_removed_broadcast_(S)',
            'send_sticky_broadcast_(S)',
            'set_preferred_applications_(S)',
            'set_time_zone_(D)',
            'set_wallpaper_(S)',
            'set_wallpaper_size_hints_(S)',
            'write_Access_Point_Name_settings_(D)',
            'write_subscribed_feeds_(D)',
            'write_sync_settings_(D)',
            'Blogger_(D)',
            'Google_App_Engine_(D)',
            'Google_Docs_(D)',
            'Google_Finance_(D)',
            'Google_Maps_(D)',
            'Google_Spreadsheets_(D)',
            'Google_Voice_(D)',
            'Google_mail_(D)',
            'Picasa_Web_Albums_(D)',
            'YouTube_(D)',
            'YouTube_usernames_(D)',
            'access_all_Google_services_(S)',
            'access_other_Google_services_(D)',
            'act_as_an_account_authenticator_(D)',
            'act_as_the_AccountManagerService_(S)',
            'contacts_data_in_Google_accounts_(D)',
            'discover_known_accounts_(S)',
            'manage_the_accounts_list_(D)',
            'read_Google_service_configuration_(S)',
            'use_the_authentication_credentials_of_an_account_(D)',
            'view_configured_accounts_(S)',
            'access_extra_location_provider_commands_(S)',
            'coarse_(network-based)_location_(D)',
            'fine_(GPS)_location_(D)',
            'mock_location_sources_for_testing_(D)',
            'Read_Email_attachments_(D)',
            'Send_Gmail_(S)',
            'edit_SMS_or_MMS_(D)',
            'modify_Gmail_(D)',
            'read_Gmail_(D)',
            'read_Gmail_attachment_previews_(D)',
            'read_SMS_or_MMS_(D)',
            'read_instant_messages_(D)',
            'receive_MMS_(D)',
            'receive_SMS_(D)',
            'receive_WAP_(D)',
            'send_SMS-received_broadcast_(S)',
            'send_WAP-PUSH-received_broadcast_(S)',
            'write_instant_messages_(D)',
            'add_or_modify_calendar_events_and_send_email_to_guests_(D)',
            'choose_widgets_(S)',
            "read_Browser's_history_and_bookmarks_(D)",
            'read_calendar_events_(D)',
            'read_contact_data_(D)',
            'read_sensitive_log_data_(D)',
            'read_user_defined_dictionary_(D)',
            'retrieve_system_internal_state_(S)',
            'set_alarm_in_alarm_clock_(S)',
            "write_Browser's_history_and_bookmarks_(D)",
            'write_contact_data_(D)',
            'write_to_user_defined_dictionary_(S)',]
    return columns



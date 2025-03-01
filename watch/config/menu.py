menu_tree = {'get_user': ['user', []], 'get_target': ['target', ['get_top_activity', 'get_sql_area', 'get_sql_stats', 'get_sql_monitor', 'get_session_monitor', 'get_plans_cache', 'get_target_waits', 'get_target_long_ops', 'get_temp_usage', 'get_undo_usage', 'get_rman_status', 'get_dml_locks']], 'get_target_snapshot': ['target', ['get_awr_report', 'get_ash_report', 'get_advisor_tasks', 'get_advisor_findings', 'get_alert_history', 'get_outstanding_alerts']], 'get_target_objects': ['target', ['get_table_stats', 'get_index_stats', 'get_segments', 'get_segment_usage', 'get_index_usage', 'get_tablespace_usage', 'get_ts_fragmentation', 'get_users', 'get_synonyms', 'get_privileges', 'get_tab_partitions_count', 'get_ind_partitions_count', 'get_modifications']], 'get_query': ['query', ['get_query_text', 'get_query_plan', 'get_query_waits', 'get_query_long_ops', 'get_query_plan_stats', 'get_query_report', 'notify_if_done']], 'get_session': ['sid', ['get_session_stats', 'notify_if_inactive']], 'get_table': ['table', ['get_table_columns', 'get_table_indexes', 'get_table_partitions', 'get_table_ddl', 'get_row_count', 'get_insert_from_select', 'get_scan_speed']], 'get_view': ['view', ['get_view_columns', 'get_view_text']]  # , 'get_task': ['target', ['wait_for_execution'
             #                            , 'wait_for_queued'
             #                            , 'check_concurrency'
             #                            , 'wait_for_heavy'
             #                            , 'check_frequent_sql'
             #                            , 'wait_for_sql_error'
             #                            , 'wait_for_session'
             #                            , 'check_session_stats'
             #                            , 'wait_for_uncommitted'
             #                            , 'wait_for_zombie'
             #                            , 'wait_for_temp'
             #                            , 'wait_for_ts'
             #                            , 'wait_for_recycled'
             #                            , 'check_size'
             #                            , 'wait_for_status'
             #                            , 'check_resource_usage'
             #                            , 'check_redo_switches'
             #                            , 'check_logs_deletion'
             #                            , 'check_job_status'
             #                            , 'wait_for_expiry'
             #                            , 'check_src_structure'
             #                            , 'ping_target']]
             , 'get_ext': ['target', []]  # , 'get_app': ['user'
             #                , ['get_notifications'
             #                   , 'get_unsent_messages'
             #                   , 'get_error_log'
             #                   , 'get_access_log']]
             , 'logout': ['user', []]}

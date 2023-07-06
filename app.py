from file_functions import log, update_archive, get_source_fname, get_lookup_filename, identify_files_for_archive, update_archive, event_logs_dir, update_fname_with_timestamp
from review_functions import extract_from_csv, identify_validated_columns, identify_null_values, identify_key, review_against_lookup
from review_functions import source_file_dir, lookup_file_dir, create_custom_lookup

if __name__ == "__main__":
    file_for_processing = get_source_fname()
    log("Starting review of data files")
    log("Starting extract")
    extracted_data = extract_from_csv(file_for_processing)
    log("Extract phase completed")

    # get info from user - validated columns from user
    validated_columns = identify_validated_columns(extracted_data)
    key_for_lookup = identify_key(extracted_data)
    lookup_filename = get_lookup_filename()

    # null values
    log(f"Starting review of source file ({file_for_processing}) for nulls in validated columns")
    validated_columns_check = identify_null_values(extracted_data, validated_columns)
    for observation in validated_columns_check:
        log(observation)
    log(f"Review of source file ({file_for_processing}) for nulls in validated columns completed")

    # review against lookup
    log("Retrieving files to review against source data")
    lookup_df = extract_from_csv(lookup_filename)
    log("Prepping files for review")
    lookup_df_dict = create_custom_lookup(lookup_df)
    log(f"Starting review of source data against lookup file {lookup_filename}")
    check_against_lookup = review_against_lookup(extracted_data, key_for_lookup, lookup_df_dict)
    for lookup_observation in check_against_lookup:
        log(lookup_observation)
    log("Review of data files completed")
    print("Review is complete")
    
    # post-review activities - rename logfile + move all used files to archive
    update_fname_with_timestamp(event_logs_dir)
    source_file_for_archive = identify_files_for_archive(source_file_dir)
    lookup_files_for_archive = identify_files_for_archive(lookup_file_dir)
    eventlogs_for_archive = identify_files_for_archive(event_logs_dir)
    update_archive(eventlogs_for_archive)
    update_archive(source_file_for_archive)
    update_archive(lookup_files_for_archive)
quit()
def api_warning_generator(api_list):
    # Print warning if endpoint is down
    for api_stat in api_list:
        if api_stat['status']:
            if api_stat['response_time'] > 0.5:
                print("{endpoint} is up with {response_time}s."
                      .format(endpoint=api_stat['endpoint'],
                              response_time=api_stat['response_time']))
            else:
                print("Warning! {endpoint} is slow with {response_time}s."
                      .format(endpoint=api_stat['endpoint'],
                              response_time=api_stat['response_time']))
        else:
            print("Warning! {endpoint} is down with {response_time}s."
                  .format(endpoint=api_stat['endpoint'],
                          response_time=api_stat['response_time']))

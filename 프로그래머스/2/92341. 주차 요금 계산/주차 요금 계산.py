def solution(fees, records):
    def _add_time(number, usetime):
        if number in total_time:
            total_time[number] += usetime
        else:
            total_time[number] = usetime
            
    def _add_charge(number, charge):
        if number in total_fee:
            total_fee[number] += charge
        else:
            total_fee[number] = charge
            
    def _calculate_charge(number, use_time):
        if use_time > default_time:
            use_time = use_time - default_time
            multiplier = use_time // per_minute if use_time % per_minute == 0 else use_time // per_minute + 1
            return default_fee + fees_per * multiplier
        else:
            return default_fee
    
    default_time, default_fee, per_minute, fees_per = fees
    total_time = {}
    total_fee = {}
    queue = {}
    final_time = 23*60 + 59
    for record in records:
        time, number, i_o = record.split(" ")
        time = time.split(":")
        time = int(time[0])*60 + int(time[1])
        if i_o == "IN":
            queue[number] = time
        elif i_o == "OUT":
            use_time = time - queue[number]
            del queue[number]
            _add_time(number, use_time)
    for number, time in queue.items():
        use_time = final_time - time
        _add_time(number, use_time)
    for number, use_time in total_time.items():
        _add_charge(number, _calculate_charge(number, use_time))
    calculated_fees = list(total_fee.items())
    calculated_fees.sort(key=lambda x: x[0])
    answer = [x[1] for x in calculated_fees]
    return answer
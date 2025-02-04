import functools

def skip_op(fn):
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        result = fn(self, *args, **kwargs)
        self._skip_op()
        
        return result
    
    return wrapper

def _parse_time(time_str):
    m, s = time_str.split(':')

    return int(m)*60 + int(s)

class Video:
    
    @skip_op
    def __init__(self, video_len, pos, op_start, op_end):
        self.video_len = _parse_time(video_len)
        self.pos = _parse_time(pos)
        self.op = (_parse_time(op_start), _parse_time(op_end))
    
    @skip_op
    def next(self):
        self.pos = min(self.video_len, self.pos+10)
    
    @skip_op
    def prev(self):
        self.pos = max(0, self.pos-10)
    
    def _skip_op(self):
        if self.op[0] <= self.pos < self.op[1]:
            self.pos = self.op[1]
    

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video = Video(video_len, pos, op_start, op_end)
    
    for comm in commands:
        if comm == "next":
            video.next()
        else:
            video.prev()
    
    answer = str(video.pos//60).zfill(2)+':'+str(video.pos%60).zfill(2)
    
    return answer
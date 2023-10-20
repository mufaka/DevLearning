from edi_segment import EdiSegment

class EdiTransaction:
    def __init__(self):
        self._segments = []

    @property
    def segments(self):
        return self._segments

    def add_raw_segment(self, raw_segment, delimiters):
        segment = EdiSegment()
        segment.populate_from_raw(raw_segment, delimiters)
        self._segments.append(segment)

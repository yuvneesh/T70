from bs4 import BeautifulSoup


def read_data(raw: str) -> dict:
    soup = BeautifulSoup(raw, "lxml-xml")

    summary = []

    for sample in soup.find_all("sample"):
        _id = str(sample.id1.string)
        _size = str(sample.size.string).split(' ')[0]
        _result = str(sample.result.result_value.string).split(' ')[0]
        _unit = str(sample.result.result_value.string).split(' ',1)[1]
        _strtDate = str(sample.sample_start.string).split('T')[0]
        _strtTime = str(sample.sample_start.string).split('T')[1]

        summary.append({
            "id": _id ,
            "size": _size, 
            "result": _result,
            "unit" : _unit,
            "start_date": _strtDate,
            "start_time": _strtTime})

    return summary
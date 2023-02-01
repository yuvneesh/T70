from bs4 import BeautifulSoup


def read_data(raw: str) -> dict:
    soup = BeautifulSoup(raw, "lxml-xml")

    summary = []

    for sample in soup.find_all("sample"):
        _id = str(sample.id1.string)
        _size = str(sample.size.string)
        _result = str(sample.result.result_value.string)
        _strtTime = str(sample.sample_start.string)

        summary.append({"id": _id ,"size": _size, "result": _result, "start_time": _strtTime})

    return summary
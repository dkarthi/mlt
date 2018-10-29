import pandas as pd


def test_run():
    start_date = '2018-01-01'
    end_date = '2018-02-09'
    dates = pd.date_range(start_date,end_date)
    df = pd.DataFrame(index=dates)
    print df

if __name__ == "__main__":
    test_run()

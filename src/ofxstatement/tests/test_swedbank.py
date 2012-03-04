import doctest

from ofxstatement.plugins.swedbank import SwedbankCsvStatementParser

def doctest_SwedbankCsvStatementParser():
    """Test SwedbankCsvStatementParser

    Open sample csv to parse
        >>> import os
        >>> csvfile = os.path.join(os.path.dirname(__file__),
        ...                        'samples', 'swedbank.csv')

    Create parser object and parse:
        >>> swedbank = SwedbankCsvStatementParser(open(csvfile, 'r'))
        >>> statement = swedbank.parse()

    Check what we've got:
        >>> statement.accountId
        'LT797300010XXXXXXXXX'
        >>> len(statement.lines)
        4
        >>> statement.startingBalance
        2123.82
        >>> statement.startingBalanceDate
        datetime.datetime(2012, 1, 1, 0, 0)
        >>> statement.endingBalance
        3917.3
        >>> statement.endingBalanceDate
        datetime.datetime(2012, 1, 31, 0, 0)
        >>> statement.currency
        'LTL'

    Check first line
        >>> l = statement.lines[0]
        >>> l.amount
        -14.34
        >>> l.payee
        "McDonald's restoranas AKR Vilnius"
        >>> l.memo
        "PIRKINYS ... 00000"
        >>> l.id
        '2012010200041787'

    Check line with awkward quotation marks:
        >>> l = statement.lines[2]
        >>> l.id
        '2012012600096815'
        >>> l.amount
        -12.2
        >>> l.payee
        'UAB "Naktida"'
        >>> l.memo
        'PIRKINYS NNNNNNNNNNNNNNNN ... UAB "Naktida" ... 00000'

    Check income line:
        >>> l = statement.lines[3]
        >>> l.id
        '2012011000673562'
        >>> l.amount
        1600.0
        >>> l.payee
        'Company'
        >>> l.memo
        'Salary'

    """



def test_suite():
    return doctest.DocTestSuite(optionflags=(doctest.NORMALIZE_WHITESPACE|
                                             doctest.ELLIPSIS|
                                             doctest.REPORT_ONLY_FIRST_FAILURE|
                                             doctest.REPORT_NDIFF
                                             ))

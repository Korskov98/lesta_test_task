import pytest
from dataclasses import dataclass

@dataclass
class ClassTestCase:
    name: str
    popularity: int
    front: list[str]
    back: list[str]
    database: list[str]


DATA = [
    ClassTestCase(name='Google', popularity=2800000000, front=['JavaScript', 'TypeScript'], back=['C', 'C++', 'Go', 'Java', 'Python', 'Node'], database=['Bigtable', 'MariaDB']),
    ClassTestCase(name='Facebook', popularity=1120000000, front=['JavaScript', 'TypeScript', 'Flow'], back=['Hack/HHVM', 'Python', 'C++', 'Java', 'Erlang', 'D', 'Haskell'], database=['MariaDB', 'MySQL', 'HBase', 'Cassandra']),
    ClassTestCase(name='Youtube', popularity=1100000000, front=['JavaScript', 'TypeScript'], back=['Python', 'C', 'C++', 'Java', 'Go'], database=['Vitess', 'BigTable', 'MariaDB']),
    ClassTestCase(name='Yahoo', popularity=750000000, front=['JavaScript'], back=['PHP'], database=['PostgreSQL', 'HBase', 'Cassandra', 'MongoDB']),
    ClassTestCase(name='Etsy', popularity=516000000, front=['JavaScript'], back=['PHP'], database=['MySQL', 'Redis']),
    ClassTestCase(name='Amazon', popularity=2400000000, front=['JavaScript'], back=['Java', 'C++', 'Perl'], database=['DynamoDB', 'RDS/Aurora', 'Redshift']),
    ClassTestCase(name='Wikipedia', popularity=475000000, front=['JavaScript'], back=['PHP'], database=['MariaDB']),
    ClassTestCase(name='Fandom', popularity=315000000, front=['JavaScript'], back=['PHP'], database=['MySQL']),
    ClassTestCase(name='X', popularity=290000000, front=['JavaScript'], back=['C++', 'Java', 'Scala', 'Ruby (Ruby On Rails)'], database=['MySQL']),
    ClassTestCase(name='Bing', popularity=285000000, front=['JavaScript'], back=['C#', 'C++'], database=['Microsoft SQL Server', 'Cosmos DB']),
    ClassTestCase(name='eBay', popularity=285000000, front=['JavaScript'], back=['Java', 'JavaScript', 'Scala'], database=['Oracle Database']),
    ClassTestCase(name='MSN', popularity=280000000, front=['JavaScript'], back=['C# (ASP.NET)'], database=['Microsoft SQL Server']),
    ClassTestCase(name='LinkedIn', popularity=260000000, front=['JavaScript'], back=['Java', 'JavaScript', 'Scala'], database=['Venice']),
    ClassTestCase(name='Pinterest', popularity=250000000, front=['JavaScript'], back=['Python (Django)', 'Erlang', 'Elixir'], database=['MySQL', 'Redis']),
    ClassTestCase(name='WordPress.com', popularity=240000000, front=['JavaScript'], back=['PHP'], database=['MariaDB']),
    ClassTestCase(name='Netflix', popularity=223090000, front=['JavaScript'], back=['Python', 'Java'], database=['NMDB', 'PostgreSQL']),
]


@pytest.mark.parametrize(
    "test_case, popular",
    [
        pytest.param(test_case, 323000000)
        for test_case in DATA
    ],
)
def test_popular(test_case, popular):
    message = test_case.name + ' (Fronted:' + ','.join(test_case.front) + '|' + 'Backend:' + ','.join(test_case.back) + ') has ' + str(test_case.popularity) + ' unique visitors per month. (Expected more than ' + str(popular) + ')'
    assert test_case.popularity > popular, message
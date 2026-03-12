# tests/unit/example_test.py
import pytest
from airflow.models import DagBag

def test_dag_loaded():
    dagbag = DagBag(dag_folder='dags/', include_examples=False)
    assert len(dagbag.dags) > 0
    assert 'example_dag' in dagbag.dags
from typing import List, Dict, Any

from etl import InstanceInfo, ETLCheck

from stackstate_checks.stubs import topology
import yaml
import logging

logging.basicConfig()
logger = logging.getLogger("stackstate_checks.base.checks.base.etl")
logger.setLevel(logging.INFO)


def test_check():
    topology.reset()
    instance_dict = setup_test_instance()
    instance = InstanceInfo(instance_dict)
    instance.validate()
    check = ETLCheck("ETL", {}, {}, instances=[instance_dict])
    check._init_health_api()
    check.check(instance)
    snapshot = topology.get_snapshot("")
    components = snapshot["components"]
    assert len(components) == 1


def setup_test_instance() -> Dict[str, Any]:
    with open("src/data/conf.d/etl.d/conf.yaml.example") as f:
        config = yaml.load(f)
        instance_dict = config["instances"][0]
    return instance_dict


def assert_component(components: List[dict], cid: str) -> Dict[str, Any]:
    component = next(iter(filter(lambda item: (item["id"] == cid), components)), None)
    assert component is not None
    return component


def assert_relation(relations: List[dict], sid: str, tid: str) -> Dict[str, Any]:
    relation = next(
        iter(
            filter(
                # fmt: off
                lambda item: item["source_id"] == sid and item["target_id"] == tid,
                # fmt: on
                relations,
            )
        ),
        None,
    )
    assert relation is not None
    return relation

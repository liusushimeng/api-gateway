from nameko.testing.services import worker_factory
from application.ci_cd_service import CICD
from context.ci_cd_context import CICDContext
from unittest.mock import MagicMock, patch
import json


def test_ci() -> None:
    # create service instance
    service = worker_factory(CICD)

    # Test func ci
    response_data = service.ci(
        project='RedAlert',
        stage='Dev',
        changesets=json.loads(open('tests/changesets.json').read()),
        rolearn='arn:aws-cn:iam::843064179036:role/aws-role-006-1000-r2-master',
        jira_id='IAC-10878',
        git_commitdesc='OAP 2.0 Git Upload Test',
        uuid='9a0ea606-4731-11ea-82a9-0242c0a8c817'
    )

    expect_response_data = {"Upload": "Success"}
    assert response_data == expect_response_data

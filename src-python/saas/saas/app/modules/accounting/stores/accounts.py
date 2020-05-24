import logging
log = logging.getLogger(__name__)

from saas.app.core.services.connection import ConnectionManager
from saas.app.core.stores.base import BaseStore

from uuid import UUID
from saas.app.modules.accounting.models.account_types import AccountTypes


class AccountsStore(BaseStore):

    def __init__(self, manager: ConnectionManager, name: str):
        super(AccountsStore, self).__init__(manager, name)

    def add(self, clientId: UUID, typeId: AccountTypes, name: str):
        '''add an account record for a specified client
        '''
        try:
            # result = super(AccountsStore, self).runProcTransactional('accounting.account_add', [clientId, typeId, name])
            result = super(AccountsStore, self).executeTransactional(
                "select * from accounting.account_add('{0}', {1}::smallint, '{2}')".format(
                    clientId,
                    typeId,
                    name
                )
            )
            return result
        except Exception as e:
            log.error(e)
            raise e
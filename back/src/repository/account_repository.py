from model.account_model import AccountModel


from model.account_type_model import AccountTypeModel

# from model.relationship.account_organization_model import AccountOrganizationModel
from model.organization_model import OrganizationModel
from model.product_type_model import ProductTypeModel
from model.team_model import TeamModel
from model.membership_model import MembershipModel

# from model.relationship.account_team_account_type_model import (
#     AccountTeamAccountTypeModel,
# )

from server import db


class AccountRepository:
    def register_account(self, username, email, password):
        new_account = AccountModel(username, email, password, 1)
        db.session.add(new_account)
        db.session.commit()
        return new_account

    def get_user_by_id(self, user_id):
        # Use a instância do SQLAlchemy aqui
        user = db.session.query(AccountModel).filter_by(id=user_id).first()
        return user

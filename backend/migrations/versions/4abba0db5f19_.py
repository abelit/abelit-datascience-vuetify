"""empty message

Revision ID: 4abba0db5f19
Revises: 
Create Date: 2020-03-24 15:03:17.799617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4abba0db5f19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block_ip',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip')
    )
    op.create_table('datapack',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('filter', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('name')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['pid'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('name')
    )
    op.create_table('menus',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.Column('module', sa.String(length=200), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('icon', sa.String(length=50), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['pid'], ['menus.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('icon'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('positions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('alias', sa.String(length=80), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('name')
    )
    op.create_table('datapack_permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('datapackid', sa.Integer(), nullable=False),
    sa.Column('permissionid', sa.Integer(), nullable=False),
    sa.Column('action', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['datapackid'], ['datapack.id'], ),
    sa.ForeignKeyConstraint(['permissionid'], ['permissions.id'], ),
    sa.PrimaryKeyConstraint('id', 'datapackid', 'permissionid')
    )
    op.create_table('groups_permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('groupid', sa.Integer(), nullable=False),
    sa.Column('permissionid', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['groupid'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['permissionid'], ['permissions.id'], ),
    sa.PrimaryKeyConstraint('id', 'groupid', 'permissionid')
    )
    op.create_table('groups_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('groupid', sa.Integer(), nullable=False),
    sa.Column('roleid', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['groupid'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['roleid'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id', 'groupid', 'roleid')
    )
    op.create_table('menus_permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('menusid', sa.Integer(), nullable=False),
    sa.Column('permissionid', sa.Integer(), nullable=False),
    sa.Column('action', sa.Integer(), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['menusid'], ['menus.id'], ),
    sa.ForeignKeyConstraint(['permissionid'], ['permissions.id'], ),
    sa.PrimaryKeyConstraint('id', 'menusid', 'permissionid')
    )
    op.create_table('roles_permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('roleid', sa.Integer(), nullable=False),
    sa.Column('permissionid', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['permissionid'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['roleid'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id', 'roleid', 'permissionid')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('alias', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('passwd', sa.String(length=200), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('groupid', sa.Integer(), nullable=False),
    sa.Column('positionid', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=1024), nullable=False),
    sa.Column('autologin', sa.Integer(), nullable=False),
    sa.Column('autologout', sa.Integer(), nullable=False),
    sa.Column('lang', sa.String(length=10), nullable=False),
    sa.Column('refresh', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('theme', sa.String(length=128), nullable=False),
    sa.Column('attempt_clock', sa.DateTime(), nullable=False),
    sa.Column('attempt_failed', sa.Integer(), nullable=False),
    sa.Column('attempt_ip', sa.String(length=64), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['groupid'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['positionid'], ['positions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=False),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('lastaccess', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('permissionid', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['permissionid'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'userid', 'permissionid')
    )
    op.create_table('users_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('roleid', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['roleid'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'userid', 'roleid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_roles')
    op.drop_table('users_permissions')
    op.drop_table('sessions')
    op.drop_table('users')
    op.drop_table('roles_permissions')
    op.drop_table('menus_permissions')
    op.drop_table('groups_roles')
    op.drop_table('groups_permissions')
    op.drop_table('datapack_permissions')
    op.drop_table('roles')
    op.drop_table('positions')
    op.drop_table('permissions')
    op.drop_table('menus')
    op.drop_table('groups')
    op.drop_table('datapack')
    op.drop_table('block_ip')
    # ### end Alembic commands ###
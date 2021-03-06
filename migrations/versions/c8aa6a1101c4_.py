"""empty message

Revision ID: c8aa6a1101c4
Revises: 4b481da8d33f
Create Date: 2021-06-17 22:04:12.432876

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c8aa6a1101c4'
down_revision = '4b481da8d33f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('description', sa.Text(), nullable=True))
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'comment')
    op.drop_constraint('downvotes_user_id_fkey', 'downvotes', type_='foreignkey')
    op.drop_constraint('downvotes_pitch_id_fkey', 'downvotes', type_='foreignkey')
    op.create_foreign_key(None, 'downvotes', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'downvotes', 'pitches', ['pitch_id'], ['id'])
    op.add_column('pitches', sa.Column('description', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_index('ix_pitches_category', table_name='pitches')
    op.create_index(op.f('ix_pitches_description'), 'pitches', ['description'], unique=False)
    op.drop_constraint('pitches_user_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['owner_id'], ['id'])
    op.drop_column('pitches', 'time')
    op.drop_column('pitches', 'user_id')
    op.drop_column('pitches', 'pitch')
    op.drop_constraint('upvotes_pitch_id_fkey', 'upvotes', type_='foreignkey')
    op.drop_constraint('upvotes_user_id_fkey', 'upvotes', type_='foreignkey')
    op.create_foreign_key(None, 'upvotes', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'upvotes', 'pitches', ['pitch_id'], ['id'])
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.create_foreign_key('upvotes_user_id_fkey', 'upvotes', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('upvotes_pitch_id_fkey', 'upvotes', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('pitches', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_user_id_fkey', 'pitches', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_index(op.f('ix_pitches_description'), table_name='pitches')
    op.create_index('ix_pitches_category', 'pitches', ['category'], unique=False)
    op.alter_column('pitches', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_column('pitches', 'owner_id')
    op.drop_column('pitches', 'description')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.create_foreign_key('downvotes_pitch_id_fkey', 'downvotes', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('downvotes_user_id_fkey', 'downvotes', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.add_column('comments', sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('comments', 'description')
    # ### end Alembic commands ###

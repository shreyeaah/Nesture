"""Fresh start for Supabase

Revision ID: c8be1de3da76
Revises: 
Create Date: 2025-06-26 16:58:01.304429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8be1de3da76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('baker_pricing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('baker_id', sa.Integer(), nullable=False),
    sa.Column('base_price_per_kg', sa.Float(), nullable=False),
    sa.Column('extra_tier_price', sa.Float(), nullable=False),
    sa.Column('frosting_prices', sa.JSON(), nullable=True),
    sa.Column('topper_prices', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['baker_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('baker_id')
    )
    op.create_table('baker_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bakery_name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('logo', sa.String(length=120), nullable=True),
    sa.Column('banner', sa.String(length=120), nullable=True),
    sa.Column('instagram', sa.String(length=150), nullable=True),
    sa.Column('facebook', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image_filename', sa.String(length=120), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('baker_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['baker_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_item_id'], ['menu_item.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('baker_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('shape', sa.String(length=20), nullable=True),
    sa.Column('tiers', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('is_custom', sa.Boolean(), nullable=True),
    sa.Column('cake_type', sa.String(length=100), nullable=True),
    sa.Column('frosting', sa.String(length=50), nullable=True),
    sa.Column('topper', sa.String(length=50), nullable=True),
    sa.Column('theme', sa.String(length=200), nullable=True),
    sa.Column('reference_img', sa.String(length=120), nullable=True),
    sa.Column('estimated_price', sa.Float(), nullable=True),
    sa.Column('delivery_mode', sa.String(length=20), nullable=False),
    sa.Column('payment_mode', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['baker_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['menu_item_id'], ['menu_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('cart_item')
    op.drop_table('menu_item')
    op.drop_table('baker_profile')
    op.drop_table('baker_pricing')
    op.drop_table('user')
    # ### end Alembic commands ###

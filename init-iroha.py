from iroha import Iroha, IrohaCrypto, IrohaGrpc
import commons

admin = commons.new_user('admin@test')
alice = commons.new_user('alice@test')
bob = commons.new_user('bob@test')
iroha = Iroha(admin['id'])


@commons.hex
def genesis_tx():
    test_permissions = [commons.primitive_pb2.can_create_account]
    genesis_commands = commons.genesis_block(admin, alice, test_permissions)
    tx = iroha.transaction(genesis_commands)
    IrohaCrypto.sign_transaction(tx, admin['key'])
    return tx


@commons.hex
def create_account_tx():
    tx = iroha.transaction([
        iroha.command('CreateAccount', account_name='bob', domain_id='test', public_key=bob['key'])
    ], creator_account=alice['id'])
    IrohaCrypto.sign_transaction(tx, alice['key'])
    return tx


if __name__ == '__main__':
    print(admin)

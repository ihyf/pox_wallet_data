from util.dbmanager import db_manager
from util.mysql_db import Transactions, Account


def add_transaction_db(from_address, to_address, tx_id, in_or_out, time_stamp):
    session = db_manager.master()
    tr = Transactions(from_address=from_address, to_address=to_address, tx_id=tx_id,
                      in_or_out=in_or_out, time_stamp=time_stamp)
    session.add(tr)
    session.commit()
    session.close()
    return tr


def get_transaction_db(address):
    session = db_manager.master()
    tr = session.query(Transactions).filter(Transactions.in_or_out == "out"
                                            and Transactions.from_address == address).order_by(-Transactions.id).first()
    session.close()
    return tr

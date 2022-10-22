import arweave
import utils 

wallet = utils.wallet



def getBalance():
    balance =  wallet.balance
    print(f"{balance} AR")

def getLastTransaction():
    lastTransaction = wallet.get_last_transaction_id()
    print(lastTransaction)

def getTransactionById():
    getTx = arweave.Transaction(wallet=wallet, id="TmcbbnWwVm003OmQflhKlLhx-kZ8kZ1eE6Cc-Csp78wW1s_q6WihabARrIl5vkY8")
    uploadTransactiondata = getTx.get_transaction()
    print(uploadTransactiondata)
    

getTransactionById()
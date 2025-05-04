from pyteal import *

def approval_program():
    return Approve()

def clear_program():
    return Approve()

if __name__ == "__main__":
    with open("ticket_approval.teal", "w") as f:
        f.write(compileTeal(approval_program(), mode=Mode.Application))

    with open("ticket_clear.teal", "w") as f:
        f.write(compileTeal(clear_program(), mode=Mode.Application))

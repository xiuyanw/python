from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
Options=namedtuple(
    'Options',[
        'connection',
        'remote_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)
options=Options(
    connection='smart',
    remote_user=None,
    ask_sudo_pass=None,
    verbosity=5,
    ask_pass=None,
    module_path=None,
    forks=5,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    listhosts=None,
    diff=False,
    listtags=None,
    listtasks=None,
    syntax=None,
    sudo_user=None,
    sudo=None
)
loader=DataLoader()
passwords=dict()
inventory=InventoryManager(loader=loader,sources=['/root/myansi/hosts'])
variable_manager=VariableManager(loader=loader,inventory=inventory)

def playbook_run(plabook_path):
    playbook=PlaybookExecutor(
        playbooks=plabook_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,options=options,passwords=passwords
 )
    result=playbook.run()
    return result
if __name__ == '__main__':
    playbook_run(plabook_path=['/root/myansi/install_web.yml'])
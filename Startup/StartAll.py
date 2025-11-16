from Startup.Docker.Network import Network
from Startup.Databases.Databases import Databases
from Startup.SDK.Backend import AssemblerPythonSDK
from Startup.Logger.Logger import GrayLog
from Startup.Orchestrator.Orchestrator import Orchestrator


network: Network = Network(network_name='assembler') # name must align with one in config
databases: Databases = Databases()
backend: AssemblerPythonSDK = AssemblerPythonSDK()
graylog: GrayLog = GrayLog()
orchestrator: Orchestrator = Orchestrator()


def run():
    network.create_if_not_exists()
    databases.pull_and_run()
    backend.run_assembler_python_sdk_if_pulled()
    graylog.pull_and_run()
    orchestrator.pull_and_run_langflow()

if __name__ == '__main__':
    run()

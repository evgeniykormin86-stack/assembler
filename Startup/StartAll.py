from Startup.Docker.Network import Network
from Startup.Databases.Databases import Databases
from Startup.SDK.Backend import AssemblerPythonSDK
from Startup.Logger.Logger import GrayLog
from Startup.Orchestrator.N8N import N8N


network: Network = Network(network_name='assembler') # name must align with one in config
databases: Databases = Databases()
backend: AssemblerPythonSDK = AssemblerPythonSDK()
graylog: GrayLog = GrayLog()
n8n: N8N = N8N()


def run():
    network.create_if_not_exists()
    databases.pull_and_run()
    backend.run_assembler_python_sdk_if_pulled()
    graylog.pull_and_run()
    n8n.pull_and_run()

if __name__ == '__main__':
    run()

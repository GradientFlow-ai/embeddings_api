import chromadb
from chromadb.config import Settings

parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

parser.add_argument('-d', '--dev', help='Turn on dev mode to run Chroma in memory')

args = parser.parse_args()
print(args)

chroma_client = chroma.Client(Settings(chroma_api_impl="rest",
                                       chroma_server_host="localhost",
                                       chroma_server_http_port="8000"
                                       ))

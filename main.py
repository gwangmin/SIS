'''
Dialogflow agent interface
Agent name: SIS(Simple Intelligent System)
'''
import sys
import lib.core as core


def main():
    '''
    Entry point
    '''
    sis = core.SISSession(session_id='test', args=sys.argv[1:])

    while True:
        _input = sis.prompt()
        print(sis.query(_input))
        sis.tts_resp()


if __name__ == "__main__":
    main()

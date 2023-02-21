from evidence import Evidence
from databaze import Databaze


databaze = Databaze()
if __name__ == '__main__':
    databaze.main()

evidence = Evidence()
evidence.main(databaze)



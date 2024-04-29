from func.check import check
from func.sort import sort

if __name__ == '__main__':
    domain = input("Try searching for a domain you like: ")
    check_availability = check(domain)
    sort_domains = sort(check_availability, domain)
def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    return s[k:n:]
print(main("codeschooluz",5,2))
print(main("apple",3,2))
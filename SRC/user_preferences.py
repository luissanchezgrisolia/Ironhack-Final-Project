def user_pre(df,name,dislikes):
    """
    Given a df, username, and a dislike list, this function introduce user data in a similiraty matrix
    """
    df.loc[name] = 0
    for ing in dislikes:
        if ing not in df.columns:
            df[ing] = 0
        df.loc[name, ing] = 200
    return df
def calculate_kpis(events):

    impressions = len(
        events[events["event_type"] == "Impression"]
    )

    clicks = len(
        events[events["event_type"] == "Click"]
    )

    purchases = len(
        events[events["event_type"] == "Purchase"]
    )

    likes = len(
        events[events["event_type"] == "Like"]
    )

    comments = len(
        events[events["event_type"] == "Comment"]
    )

    shares = len(
        events[events["event_type"] == "Share"]
    )

    ctr = (
        clicks / impressions * 100
        if impressions > 0
        else 0
    )

    conversion_rate = (
        purchases / clicks * 100
        if clicks > 0
        else 0
    )

    engagement_rate = (
        (likes + comments + shares)
        / impressions
        * 100
        if impressions > 0
        else 0
    )

    overall_conversion = (
        purchases / impressions * 100
        if impressions > 0
        else 0
    )

    return {
        "impressions": impressions,
        "clicks": clicks,
        "purchases": purchases,
        "ctr": ctr,
        "conversion_rate": conversion_rate,
        "engagement_rate": engagement_rate,
        "overall_conversion": overall_conversion
    }

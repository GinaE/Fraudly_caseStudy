<center><h3>Feature Dictionary</h3></center>
* ```acct_type```	fraudster_event, fraudster, and fraudster_att are fraud

* ```approx_payout_date```:    int, presumably timestamp
* ```body_length```        Number of chars in description field, but not always (??)
* ```channels```            Unknown. 8, 0, 5, 11, 6 are common values, max is 13
* ```country```            Country of users; sometimes blank; usually English-speaking
* ```currency```            Currency of transaction; Usually dollars, pounds, Canadian Dollars
* ```delivery_method```        Preferred method of delivery? Could be 0, 1, or 3
* ```description```        Description of event; lots of text and html!
* ```email_domain```       Domain of poster. Gmail is most common, but only makes up 3000.
* ```event_created```        Timestamp; come back to this
* ```event_end```        Timestamp; come back to this
* ```event_published```        Timestamp; come back to this
* ```event_start```        Timestamp; come back to this    
* ```fb_published```        0 or 1; usually 0
* ```gts```            Some float; mean is 2430 but median is 431!
* ```has_analytics```        0 or 1; usually 0
* ```has_header```        0 or 1; often missing
* ```has_logo```            0 or 1; often 1
* ```listed```            y or n; usually y
* ```name```            Name of event; text
* ```name_length```        Len of name field
* ```num_order```        Presumably number of orders buyer made? Median is 8, mean is 28
* ```num_payouts```        Presumably number of payouts by…; Median is 2, mean is 33
* ```object_id```            Unique identifier
* ```org_desc```            Description of organization, often missing
* ```org_facebook```        Mean is 8, but some non-numerics screwing up the math
* ```org_name```        Organization making posting
* ```org_twitter```        Mean is around 4
* ```payee_name```        Name of lister
* ```payout_type```        ACH or check
* ```previous_payouts```        List of dictionaries, each of which has info about previous payout
* ```sale_duration```        Number of days post was up?
* ```sale_duration2```        Number of days post was up?
* ```show_map```        Whether the map was shown? Usually 1
* ```ticket_types```        List of dictionaries of ticket types, has info about costs, etc.    
* ```user_age```            Number of days account if seller exists?
* ```user_created```        timestamp of when event was created (can use to figure out age, &c?)
* ```user_type```            Can be an int: 3, 1, 4, 5, 103???, 2
* ```venue_address```        Address of venue!
* ```venue_country```        Country of venue!
* ```venue_latitude```        Long
* ```venue_longitude```        Lat
* ```venue_name```        Name of venue
* ```venue_state```        State of venue
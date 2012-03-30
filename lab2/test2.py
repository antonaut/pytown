#!/usr/bin/env python3
"""Ska ge output:
{user_id, email, address, uname, companyid}
{user_id, task_id, taskdescription}
{company_id, company_desc, com_name}
{asset, task, asset_desc, assetname}
{a, b, c, d, e}
{task_id, company_id, asset, a}
"""
from fdutils import *
from fd import Functional_Dependencies as FD


S_facebook = {FD({'user_id'},{'email','adress','uname','companyid'}),FD({'task_id'},{'taskdescription','user_id'}),FD({'company_id'},{'company_desc','com_name'}),FD({'asset'},{'task','asset_desc','asset_name'}),FD({'a'},{'b','c','d','e'})}
B_facebook = BCNF(S_facebook)
print(B_facebook)

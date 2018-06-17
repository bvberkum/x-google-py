credentials = get_credentials(APPLICATION_NAME, opts.flags.secret,
            CRED_FILE, SCOPES)
http = credentials.authorize(httplib2.Http())
service = discovery.build('blogger', 'v3', http=http)


r = service.blogs().listByUser(userId='self').execute()
print(r.keys())

for i in r['items']:
    b = confparse.Values(i)
    print(i.keys())
    print(b.url, b.name)

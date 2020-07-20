This is a working example of a multi-container flask application with postgres, mongo and redis as the database fronted by the nginx reverse proxy.

## Usage

1. Bring up the cluster
```bash
$ docker-compose up -d
```

3. Browse to localhost:8181 to see the app in action.
2. Browse to localhost:5151 to see the postgres manager.

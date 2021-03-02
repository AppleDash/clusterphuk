import toml

class VMConfig:
    def __init__(self, path):
        with open(path, 'r') as fp:
            config = toml.load(fp)

        keys = list(config.keys())

        if len(keys) != 1:
            raise ValueError('Top-level VM config must have exactly one key')

        self.name = keys[0]
        self.config = config[self.name]

    def merge_from(self, other):
        for key, value in other.config.items():
            if key not in self.config:
                self.config[key] = value

    def __getitem__(self, item):
        return self.config[item]

    def __repr__(self):
        return repr(self.config)

    def __str__(self):
        return str(self.config)

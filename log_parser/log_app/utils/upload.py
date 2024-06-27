import datetime as dt

from inspect import stack as inspect_stack
from os import path

from log_app.models import Log, Message


class LogUploader():
    def _get_file(self, file_path):
        if path.isabs(file_path):
            file_path = file_path
        else:
            calling_script_dir = path.dirname(inspect_stack()[1].filename)
            file_path = path.join(calling_script_dir, file_path)
        return file_path

    def _process(self, lines):
        for line in lines:
            split_line = line.upper().split()
            try:
                line_date = dt.datetime.strptime(
                    f'{split_line[0]} {split_line[1]}', '%Y-%m-%d %H:%M:%S'
                )
            except ValueError:
                continue
            log_str = ' '.join(split_line[3:])
            address = split_line[4] if split_line[3] in ['<=', '==', '=>', '->', '==', '**'] else ''
            if 'BLACKHOLE' in address:
                address = split_line[5][1:-1]
            if split_line[3] != '<=':
                Log.objects.create(
                    created=line_date,
                    int_id=split_line[2],
                    log_str=log_str,
                    address=address
                )
            else:
                in_log_id = split_line[-1] if 'ID=' in split_line[-1] else ''
                Message.objects.create(
                    created=line_date,
                    in_log_id=in_log_id,
                    int_id=split_line[2],
                    log_str=log_str
                )
        return

    def handle(self, options):
        lines = []
        file_path = self._get_file(options.get('file'))
        with open(file_path, 'r') as file:
            lines = [line for line in file]
        self._process(lines)
        return

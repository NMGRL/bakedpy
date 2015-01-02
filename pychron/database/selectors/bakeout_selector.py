# ===============================================================================
# Copyright 2011 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
from pychron.database.orms.bakeout_orm import BakeoutTable
from pychron.database.core.database_selector import DatabaseSelector
from pychron.database.core.query import BakeoutQuery
from pychron.database.records.bakeout_record import BakeoutRecordView, BakeoutRecord


class BakeoutDBSelector(DatabaseSelector):
    query_table = BakeoutTable
    record_view_klass = BakeoutRecordView
    query_klass = BakeoutQuery
    lookup = {'Run Date': ([], BakeoutTable.timestamp), }
    dclick_recall_enabled = True

    def _make_record(self, record_view):
        db = self.db
        with db.session_ctx():
            dbrecord = db.get_bakeout(record_view.record_id)
            r = BakeoutRecord(dbrecord)

        return r

    def _get_selector_records(self, queries=None, limit=None, **kw):
        with self.db.session_ctx() as sess:
            q = sess.query(self.query_table)
            return self._get_records(q, queries, limit)

# ============= EOF =============================================


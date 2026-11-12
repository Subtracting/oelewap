import test from 'node:test';
import assert from 'node:assert/strict';
import politicians from '../src/politicians.json' with { type: 'json' };
import { pickNextProfile } from '../src/profile-picker.js';

const profiles = [{ id: 'a' }, { id: 'b' }, { id: 'c' }];
const namedProfiles = [{ name: 'First' }, { name: 'Second' }, { name: 'Third' }];

test('chooses an unseen profile before repeating a previous one', () => {
  assert.equal(pickNextProfile(profiles, ['a', 'b'], () => 0).id, 'c');
});

test('chooses an unseen profile when profile names are used as keys', () => {
  assert.equal(pickNextProfile(namedProfiles, ['First', 'Second'], () => 0).name, 'Third');
});

test('does not immediately repeat the last profile after the full collection cycles', () => {
  const next = pickNextProfile(profiles, ['a', 'b', 'c'], () => 0);
  assert.equal(next.id, 'a');
  assert.notEqual(next.id, 'c');
});

test('returns null for an empty profile collection', () => {
  assert.equal(pickNextProfile([], [], () => 0), null);
});

test('gives each politician a distinct, short Dutch roast', () => {
  const roasts = politicians.map(person => person.roast?.trim()).filter(Boolean);
  assert.equal(roasts.length, politicians.length);
  assert.equal(new Set(roasts).size, politicians.length);
  assert.ok(roasts.every(roast => roast.length <= 90));
});

test('ignores history entries not present in the collection', () => {
  assert.equal(pickNextProfile(profiles, ['missing'], () => 0).id, 'a');
});

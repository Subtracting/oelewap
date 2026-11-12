import test from 'node:test';
import assert from 'node:assert/strict';
import politicians from '../src/politicians.json' with { type: 'json' };
import { pickNextProfile } from '../src/profile-picker.js';
import portraits from '../src/portrait-sources.json' with { type: 'json' };

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

test('includes at least twenty current Tweede Kamer members with credited official portraits', () => {
  assert.ok(politicians.length >= 20, `Expected at least 20 active members, got ${politicians.length}`);
  const roasts = politicians.map(person => person.roast?.trim());
  assert.equal(new Set(politicians.map(person => person.name)).size, politicians.length);
  assert.ok(roasts.every(Boolean), 'Every parliament profile needs its own roast');
  for (const person of politicians) {
    assert.ok(person.imageWidth >= 800, `${person.name} needs a high-resolution portrait`);
    assert.ok(person.file?.startsWith('https://commons.wikimedia.org/wiki/File:'), `${person.name} needs a linked Commons attribution`);
    assert.ok(portraits.some(image => image.file === person.file && image.width >= person.imageWidth), `${person.name} is missing verified source dimensions`);
    assert.ok(person.credit && person.file, `${person.name} needs portrait attribution`);
    assert.ok(person.image?.startsWith('https://'), `${person.name} is missing a portrait URL`);
    assert.ok(person.tweedekamer?.startsWith('https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden/'), `${person.name} is missing an official member page`);
  }
});

test('ignores history entries not present in the collection', () => {
  assert.equal(pickNextProfile(profiles, ['missing'], () => 0).id, 'a');
});

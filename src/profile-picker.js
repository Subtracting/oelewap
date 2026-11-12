export function pickNextProfile(profiles, seenIds = [], random = Math.random) {
  if (profiles.length === 0) return null;

  const getId = profile => profile.id ?? profile.name;
  const seen = new Set(seenIds);
  let candidates = profiles.filter(profile => !seen.has(getId(profile)));
  if (candidates.length === 0) {
    const lastId = seenIds.at(-1);
    candidates = profiles.filter(profile => getId(profile) !== lastId);
  }
  if (candidates.length === 0) candidates = profiles;

  const index = Math.min(candidates.length - 1, Math.floor(random() * candidates.length));
  return candidates[index];
}

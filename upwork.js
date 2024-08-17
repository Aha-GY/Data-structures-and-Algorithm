function findCombinationsFromText(text) {
    // Clean the input by removing any non-standard characters
    let cleanedText = '';
    for (let i = 0; i < text.length; i++) {
        let ch = text.charAt(i);
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9') || ch === '_' || ch === '-' || ch === ',') {
            cleanedText += ch;
        }
    }

    // Split the input into individual tags based on commas or dashes
    const parts = cleanedText.split(',');
    const tags = [];
    parts.forEach(part => {
        tags.push(...part.split('-').map(tag => tag.trim()).filter(tag => tag.length > 0));
    });

    // Define the hierarchy order
    const hierarchy = ['Group', 'Category', 'Subcategory', 'Make', 'Model', 'Diagram'];

    // Sort the tags according to the defined hierarchy
    const sortedTags = tags.sort((a, b) => {
        const aIndex = hierarchy.findIndex(h => a.startsWith(h));
        const bIndex = hierarchy.findIndex(h => b.startsWith(h));
        return aIndex - bIndex;
    });

    // Filter out any tags that don't follow the hierarchy or are duplicates
    const validTags = [];
    const seen = new Set();

    for (const tag of sortedTags) {
        const prefix = tag.split('_')[0];
        if (hierarchy.includes(prefix) && !seen.has(prefix)) {
            seen.add(prefix);
            validTags.push(tag);
        }
    }

    // Generate all combinations based on the valid tags
    const combinations = [];
    const generateCombinations = (index, current) => {
        if (index === validTags.length) {
            if (current.length > 0) {
                combinations.push([...current]);
            }
            return;
        }
        // Include the current tag
        generateCombinations(index + 1, current.concat(validTags[index]));
        // Exclude the current tag
        generateCombinations(index + 1, current);
    };

    generateCombinations(0, []);

    return combinations;
}


